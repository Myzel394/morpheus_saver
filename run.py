from pyyoutube import Api, Comment
import urllib.parse
from constants import *


def build_comment_link(video_id: str, comment_id: str) -> str:
    url = "https://youtube.com/watch?"
    data = {
        "v": video_id,
        "lc": comment_id
    }
    
    full_url = url + urllib.parse.urlencode(data)
    
    return full_url


def main():
    api = Api(
        api_key=API_KEY,
        client_secret=CLIENT_SECRET,
        client_id=CLIENT_ID,
    )
    
    comments = api.get_comment_threads(all_to_channel_id=CHANNEL_ID, count=SEARCH_AMOUNT).items
    comments_with_replies = [
        comment
        for comment in comments
        if comment.replies
    ]
    
    for comment in comments_with_replies:
        is_faker = False
        has_already_been_informed = False
        
        # Check if there is a fake account in a reply
        for reply in comment.replies.comments:
            reply_name = reply.snippet.authorDisplayName
            reply_id = reply.snippet.authorChannelId
            
            if reply_name.lower() in FAKE_NAMES:
                # Check if it's a faker
                if reply_id.value != CHANNEL_ID:
                    # Faker found!
                    is_faker = True
            
            if reply.snippet.textOriginal == NOTIFY_MESSAGE:
                has_already_been_informed = True
        
        if is_faker and not has_already_been_informed:
            video_id = comment.snippet.videoId
            comment_id = comment.id
            url = build_comment_link(video_id, comment_id)
            
            print(f"Faker found on video {url}")
            
            
            # Write comment logic should be here
    

if __name__ == "__main__":
    main()
