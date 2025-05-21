
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp import FastMCP
from googleapiclient.discovery import build
from transformers import pipeline
import os
from dotenv import load_dotenv
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

load_dotenv()


# YouTube API Setup
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Initialize the MCP server with a friendly name
mcp = FastMCP("Community Chatters")

LABELS = {
    "POS": "positive",
    "NEU": "neutral",
    "NEG": "negative"
}

@mcp.tool()
def video_comments(video_id: str):  # Add type hint for parameter
    """Fetch comments from a YouTube video"""
    comments_data = []
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    try:
        video_response = youtube.commentThreads().list(
            part='snippet,replies',
            videoId=video_id
        ).execute()
        
        while video_response:
            for item in video_response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments_data.append(comment)
            
            if 'nextPageToken' in video_response:
                video_response = youtube.commentThreads().list(
                    part='snippet,replies',
                    videoId=video_id,
                    pageToken=video_response['nextPageToken']
                ).execute()
            else:
                break
    except Exception as e:
        return f"Error fetching comments: {str(e)}"
    
    return comments_data

@mcp.tool()
def sentiment_analysis(comments_data: list):
    """Analyze sentiment of comments using HuggingFace model"""
    results = []
    try:
        analyzer = pipeline(
            "sentiment-analysis", 
            model="finiteautomata/bertweet-base-sentiment-analysis",
            token=HUGGINGFACE_API_KEY
        )
        
        for comment in comments_data:
            clean_comment = comment.strip().replace("\n", " ")[:120]
            result = analyzer(clean_comment)
            label = LABELS.get(result[0]["label"], "unknown")
            results.append({"comment": clean_comment, "sentiment": label})
            
    except Exception as e:
        return f"Error analyzing sentiment: {str(e)}"
    
    return results



# Run the MCP server locally
if __name__ == '__main__':
    mcp.run()