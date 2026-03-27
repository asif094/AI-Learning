from git import Repo

def clone_repo(url, path="./repo"):
    return Repo.clone_from(url, path)

def commit_and_push(repo_path, message="AI update"):
    repo = Repo(repo_path)
    repo.git.add(A=True)
    repo.index.commit(message)
    repo.remote().push()