import praw,sys

def main():

    #redirect to log file
    sys.stdout = open('log.txt', 'w')

    # obtain a reddit instance
    reddit = praw.Reddit(client_id='f2gYedRGChaUFsrQ',
                        client_secret='iJwwmN1GkxLHU_CYnMXqXtDlPWs',
                        user_agent='my user agent',
                        username='DialogueDataset',
                        password='comp551')

    DFS(reddit.subreddit("catalonia").top('all'))

def DFS(subreddit):
    for submission in subreddit:
        submission.comments.replace_more(limit=0)
        for top_level_comment in submission.comments:
            print(top_level_comment.body)
        '''
        if len(submission.comments)>0:
            visited = set([])
            stack = []
            stack.append(submission.comments.__getitem__(0))
            while stack:
                current = stack.pop()
                print(current)
                visited.add(current)
                add_to_XML(current)
                for reply in current.replies:
                    stack.append(reply)
        '''


#placeholder
def add_to_XML(comment):
    return None

if __name__ == "__main__":
    main()