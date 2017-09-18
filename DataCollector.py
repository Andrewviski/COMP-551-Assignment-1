import praw,sys,time

reload(sys)
sys.setdefaultencoding('utf-8')

ofile = open("log.xml", "w")

def main():

    reddit = praw.Reddit(client_id='OlfGGYW2I06cVQ',
                        client_secret='FneP5eGqBL1x3pV0GifzbieYy_E',
                        user_agent='my user agent',
                        username='DialogueDataset',
                        password='comp551')
    
    english_file= open("frequentWords.txt", "r")
    english_submission_words = [line.rstrip('\n') for line in english_file]
    english_file.close()
    common_submission_words = set(english_submission_words[:20]) #0-100
    
    subreddit_file =open("SpanishSubreddits.txt","r")
    for line in subreddit_file :
        line=line.replace('\n',"")

        subreddit=reddit.subreddit(line).top('all')
        print("Extracting " + line + "(" + subreddit.url + ")" + " Subreddit...")
        DFS(subreddit, common_submission_words)
        print("Done Extracting " + line +"!\n\n")
        print('-----------------------------=============================================-----------------------------')
        subreddit_file.close()

def parse_replies(comment,users,uid):
    for reply in comment.replies:
        if (reply.author is not None) and (not reply.author.name in users):
            users[reply.author.name]=uid
            uid+=1

        if reply.author is not None:
            ofile.write("<utt uid=\"" + str(users[reply.author.name]) + "\">")
            ofile.write(reply.body)
            ofile.write("</utt>")

            reply.replies.replace_more(limit=0)
            for reply2 in reply.replies:
                parse_replies(reply2,users,uid)

def DFS(subreddit, filter_set):
     for submission in subreddit:
        if is_correct_language(submission.title, filter_set):
            print("["+submission.title+"]: ( url: "+submission.url+" ) {id: "+submission.id+" }")
            ofile.write("<dialog>")
            submission.comments.replace_more(limit=0)
            for comment in submission.comments:
                ofile.write("<s>")
                users={}
                if comment.author is not None:
                    users[comment.author.name]=0
                    ofile.write("<utt uid=\""+str(users[comment.author.name])+"\">")
                    ofile.write(comment.body)
                    ofile.write("</utt>")
                parse_replies(comment,users,1)
                ofile.write("</s>")
            ofile.write("</dialog>")

def is_correct_language(submission_words,filter_set):
    for word in submission_words:
        if word in filter_set:
            return false
    return True

if __name__ == "__main__":
    main()