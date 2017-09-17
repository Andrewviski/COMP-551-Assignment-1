import praw

def main():
    # obtain a reddit instance
    reddit = praw.Reddit(client_id='f2gYRGChaUFsrQ',
                        client_secret='iJwwmN1GkxLHU_CYnMXqXtDlPWs',
                        user_agent='my user agent',
                        username='DialogueDataset',
                        password='comp551')

    '''
    with open("SpanishSubreddits.txt") as file:
        for line in file:
            parse(line)
    file.close()
    '''
    DFS("catalunya")

def DFS(subreddit):
    for submission in reddit.subreddit(subreddit).top('all'):
        visited = Set([])
        stack = []
        submission.comments.replace_more(limit=0)  
        stack.append(submission.comments[1])
        while not stack:
            current = stack.pop()
            visited.add(current)
            add_to_XML(current)
            for reply in comment.replies:
                stack.append(reply)

#placeholder
def add_to_XML(comment):
    return None

if __name__ == "__main__":
    main()