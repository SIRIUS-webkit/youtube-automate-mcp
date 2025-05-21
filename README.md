# MCP Analysis

A Python-based tool for analyzing YouTube video comments and performing sentiment analysis.

## Features

- Fetch comments from YouTube videos using video IDs
- Perform sentiment analysis on comments using HuggingFace models
- Extract and display top positive comments
- Easy-to-use interface for analyzing social media engagement

## Prerequisites

- Python 3.x
- Required Python packages (install via pip):
  ```bash
  pip install -r requirements.txt
  ```

## Installation

1. Clone the repository:

   ```bash
   git clone [your-repository-url]
   cd mcp-analysis
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Analyzing YouTube Comments

To analyze comments from a YouTube video:

```python
# Example code usage
from mcp_analysis.video_comments import get_video_comments
from mcp_analysis.sentiment_analysis import analyze_sentiment

# Get video comments
video_id = "your_video_id"
comments = get_video_comments(video_id)

# Perform sentiment analysis
sentiment_results = analyze_sentiment(comments)
```

## Project Structure

```
mcp-analysis/
├── mcp_analysis/
│   ├── __init__.py
│   ├── video_comments.py
│   └── sentiment_analysis.py
├── requirements.txt
└── README.md
```

## Features in Detail

### YouTube Comment Fetching

- Retrieves comments from YouTube videos using video IDs
- Handles pagination and API limits
- Filters out spam and inappropriate content

### Sentiment Analysis

- Uses HuggingFace models for accurate sentiment analysis
- Categorizes comments as positive, negative, or neutral
- Provides confidence scores for sentiment classifications

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- HuggingFace for providing sentiment analysis models
- YouTube Data API for enabling comment retrieval
- All contributors who have helped to improve this project

## Contact

Your Name - [your-email@example.com]
Project Link: [https://github.com/yourusername/mcp-analysis]
