import datetime
import getpass
from github import Github

username = input("Enter GitHub username: ")
pw = getpass.getpass()

g = Github(username, pw)

def get_commits(username, repo_name):
    '''
    username : 'kshitij10496'
    repo_name : 'kshitij10496/IIKH'
                'sympy/sympy'
    '''
    total_commits = 0
    total_additions, total_deletions, total_changes = 0, 0, 0
    
    user = g.get_user(username)
    repo = g.get_repo(repo_name)
    starting_date = datetime.datetime(2016, 5, 1)
    ending_date = datetime.datetime(2016, 12, 31)
    all_commits = repo.get_commits(author=username)#, since=starting_date, until=ending_date)
    for commit in all_commits:
        total_additions += int(commit.stats.additions)
        total_deletions += int(commit.stats.deletions)
        total_changes += int(commit.stats.total)
        total_commits += 1

    print("Total commits: " + str(total_commits))
    print("Total additions: " + str(total_additions))
    print("Total deletions: " + str(total_deletions))
    print("Total changes: " + str(total_changes))

if __name__ == '__main__':
    get_commits('kshitij10496', 'sympy/sympy')