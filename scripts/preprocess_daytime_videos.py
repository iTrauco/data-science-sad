#!/usr/bin/env python3
# preprocess_daytime_videos.py
import cv2
import os
import json
import numpy as np
from datetime import datetime
import argparse
from pathlib import Path

def assess_frame_quality(frame):
    """calculate frame quality metrics"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    blur_score = laplacian.var()
    return brightness, blur_score

def process_video(video_path, output_dir, sample_fps=2, duration=60):
    """process single video file"""
    # open video
    cap = cv2.VideoCapture(str(video_path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # sampling interval
    sample_interval = int(fps / sample_fps)
    frames_to_read = int(fps * duration)
    
    # extract and process
    processed_frames = []
    frame_count = 0
    
    for i in range(frames_to_read):
        ret, frame = cap.read()
        if not ret:
            break
            
        # sample frame
        if i % sample_interval == 0:
            brightness, blur_score = assess_frame_quality(frame)
            
            # quality threshold
            if brightness > 30 and blur_score > 100:
                processed_frames.append({
                    'frame': frame,
                    'index': frame_count,
                    'brightness': brightness,
                    'blur_score': blur_score
                })
                frame_count += 1
    
    cap.release()
    
    # save frames
    os.makedirs(output_dir, exist_ok=True)
    video_name = video_path.stem
    timestamp = video_name.split('_')[2]
    
    for data in processed_frames:
        frame_name = f"frame_{timestamp}_{data['index']:03d}.jpg"
        frame_path = os.path.join(output_dir, frame_name)
        cv2.imwrite(frame_path, data['frame'], [cv2.IMWRITE_JPEG_QUALITY, 85])
    
    # save metadata
    metadata = {
        'source_video': video_path.name,
        'processing_time': datetime.now().isoformat(),
        'fps_original': float(fps),
        'fps_sampled': sample_fps,
        'duration_seconds': duration,
        'total_frames': len(processed_frames),
        'quality_stats': {
            'avg_brightness': float(np.mean([f['brightness'] for f in processed_frames])) if processed_frames else 0,
            'avg_blur_score': float(np.mean([f['blur_score'] for f in processed_frames])) if processed_frames else 0,
            'min_brightness': float(np.min([f['brightness'] for f in processed_frames])) if processed_frames else 0,
            'min_blur_score': float(np.min([f['blur_score'] for f in processed_frames])) if processed_frames else 0
        }
    }
    
    metadata_path = os.path.join(output_dir, 'metadata.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return len(processed_frames)

def find_all_13_videos(base_path, target_hour=13):
    """Find all videos from target hour across all cameras and dates"""
    base_path = Path(base_path)
    videos = []
    
    # Scan all camera directories
    for camera_dir in base_path.iterdir():
        if camera_dir.is_dir() and camera_dir.name.startswith('ATL-'):
            
            # Scan all date directories
            for date_dir in camera_dir.iterdir():
                if date_dir.is_dir():
                    
                    # Find videos from target hour
                    for video_file in date_dir.glob("*.mp4"):
                        # Extract hour from filename
                        time_str = video_file.name.split('_')[2][:2]
                        if int(time_str) == target_hour:
                            videos.append({
                                'path': video_file,
                                'camera': camera_dir.name,
                                'date': date_dir.name,
                                'file': video_file.name
                            })
    
    return videos

if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser(description='Extract frames from all traffic videos at 13:00 EST')
    parser.add_argument('--base-path', default='/home/trauco/traffic-recordings', 
                        help='Base path to traffic recordings')
    parser.add_argument('--output-base', default='../frames', 
                        help='Base output directory for frames')
    parser.add_argument('--hour', type=int, default=13, 
                        help='Hour to process (0-23, default: 13 for 1 PM EST)')
    parser.add_argument('--sample-fps', type=int, default=2,
                        help='Sample rate in fps (default: 2)')
    parser.add_argument('--duration', type=int, default=60,
                        help='Duration to process in seconds (default: 60)')
    
    args = parser.parse_args()
    
    # Find all videos from target hour
    print(f"Scanning for all videos from {args.hour}:00 EST...")
    videos = find_all_13_videos(args.base_path, args.hour)
    
    # Group by camera for summary
    from collections import defaultdict
    camera_summary = defaultdict(int)
    for v in videos:
        camera_summary[v['camera']] += 1
    
    print(f"\nFound {len(videos)} total videos from {args.hour}:00 EST:")
    for camera, count in sorted(camera_summary.items()):
        print(f"  {camera}: {count} videos")
    
    # Process all videos
    print(f"\nProcessing all {len(videos)} videos...")
    total_frames = 0
    
    for i, video_info in enumerate(videos):
        video_path = video_info['path']
        camera_id = video_info['camera']
        date = video_info['date']
        
        # Maintain same directory structure
        output_dir = os.path.join(args.output_base, camera_id, date, video_path.stem)
        
        print(f"\n[{i+1}/{len(videos)}] Processing {camera_id}/{date}/{video_info['file']}...")
        frames = process_video(video_path, output_dir, args.sample_fps, args.duration)
        print(f"  -> Saved {frames} frames")
        total_frames += frames
    
    print(f"\n✓ Processing complete!")
    print(f"  Total videos processed: {len(videos)}")
    print(f"  Total frames extracted: {total_frames}")