#!/usr/bin/env python3
# preprocess_videos.py
import cv2
import os
import json
import numpy as np
from datetime import datetime
import argparse

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
    cap = cv2.VideoCapture(video_path)
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
    video_name = os.path.basename(video_path).split('.')[0]
    timestamp = video_name.split('_')[2]
    
    for data in processed_frames:
        frame_name = f"frame_{timestamp}_{data['index']:03d}.jpg"
        frame_path = os.path.join(output_dir, frame_name)
        cv2.imwrite(frame_path, data['frame'], [cv2.IMWRITE_JPEG_QUALITY, 85])
    
    # save metadata
    metadata = {
        'source_video': os.path.basename(video_path),
        'processing_time': datetime.now().isoformat(),
        'fps_original': float(fps),
        'fps_sampled': sample_fps,
        'duration_seconds': duration,
        'total_frames': len(processed_frames),
        'quality_stats': {
            'avg_brightness': float(np.mean([f['brightness'] for f in processed_frames])),
            'avg_blur_score': float(np.mean([f['blur_score'] for f in processed_frames])),
            'min_brightness': float(np.min([f['brightness'] for f in processed_frames])),
            'min_blur_score': float(np.min([f['blur_score'] for f in processed_frames]))
        }
    }
    
    metadata_path = os.path.join(output_dir, 'metadata.json')
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return len(processed_frames)

if __name__ == "__main__":
    # parse arguments
    parser = argparse.ArgumentParser(description='Extract frames from traffic videos')
    parser.add_argument('camera_id', help='Camera ID (e.g., ATL-0972)')
    parser.add_argument('--date', default='2025-06-09', help='Date folder (YYYY-MM-DD)')
    parser.add_argument('--limit', type=int, default=0, help='Limit number of videos to process')
    
    args = parser.parse_args()
    
    # paths
    base_path = "/home/trauco/traffic-recordings"
    videos_path = os.path.join(base_path, args.camera_id, args.date)
    output_base = "../frames"  # go up one level from scripts/
    
    # get video files
    video_files = [f for f in os.listdir(videos_path) if f.endswith('.mp4')]
    video_files = sorted(video_files)
    
    if args.limit > 0:
        video_files = video_files[:args.limit]
    
    print(f"Processing {len(video_files)} videos from {args.camera_id}")
    
    # process each video
    for i, video in enumerate(video_files):
        video_path = os.path.join(videos_path, video)
        video_id = video.split('.')[0]
        output_dir = os.path.join(output_base, args.camera_id, args.date, video_id)
        
        print(f"[{i+1}/{len(video_files)}] Processing {video}...")
        frames = process_video(video_path, output_dir)
        print(f"  -> Saved {frames} frames")