import os
import tempfile
import ffmpeg
from thumbnails.processors import BaseProcessor
from django.core.files.base import ContentFile
from PIL import Image

class VideoThumbnailProcessor(BaseProcessor):
    """
    Processor for creating WebP thumbnails from video files.
    """
    
    def process(self, source, **kwargs):
        width = kwargs.get('width', 320)
        height = kwargs.get('height', 240)
        time_offset = kwargs.get('time', 2.5)  # Capture frame at 2.5 seconds by default
        webp_quality = kwargs.get('quality', 80)  # WebP quality (0-100)
        
        # Use a JPG as temporary file since ffmpeg may have issues with direct WebP output
        with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
            temp_thumbnail = temp_file.name
        
        try:
            # Create a temporary file to store the downloaded video
            with tempfile.NamedTemporaryFile(suffix=os.path.splitext(source.name)[1], delete=False) as temp_video_file:
                temp_video = temp_video_file.name
                
                # If source is a file-like object from S3, download it
                if hasattr(source, 'read'):
                    temp_video_file.write(source.read())
                    # Reset file pointer in case we need to read again
                    if hasattr(source, 'seek'):
                        source.seek(0)
                # If it's a string path, use it directly (unlikely with S3)
                else:
                    temp_video = source
            
            # Use ffmpeg to extract a thumbnail at the specified time
            (
                ffmpeg
                .input(temp_video, ss=time_offset)
                .output(temp_thumbnail, vframes=1, format='image2', vf=f'scale={width}:{height}')
                .overwrite_output()
                .run(quiet=True)
            )
            
            # Open the image with PIL and convert to WebP
            with Image.open(temp_thumbnail) as img:
                img = img.convert('RGB')
                # Create a ContentFile to store the WebP image
                output = ContentFile(b'')
                # Save as WebP with the specified quality and method 6 (better compression)
                img.save(output, format='WEBP', quality=webp_quality, method=6, lossless=False)
                output.seek(0)  # Reset file pointer
                
            # Clean up temporary files
            if os.path.exists(temp_thumbnail):
                os.unlink(temp_thumbnail)
            if os.path.exists(temp_video) and temp_video != source:  # Don't delete the original if it's a path
                os.unlink(temp_video)
            
            return output
            
        except Exception as e:
            # Clean up on error
            if os.path.exists(temp_thumbnail):
                os.unlink(temp_thumbnail)
            if os.path.exists(temp_video) and temp_video != source:
                os.unlink(temp_video)
            # Re-raise with more information
            raise Exception(f"WebP thumbnail generation failed: {str(e)}")
