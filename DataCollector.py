import praw

# obtain a reddit instance
reddit = praw.Reddit(client_id='f2gYRGChaUFsrQ',
                    client_secret='iJwwmN1GkxLHU_CYnMXqXtDlPWs',
                    user_agent='my user agent',
                    username='DialogueDataset',
                    password='comp551')

# trying to play around with some random subreddit
for submission in reddit.subreddit('learnpython').hot(limit=10):
    print(submission.title)
    print(submission.score)
    print(submission.id)