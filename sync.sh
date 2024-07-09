echo git fetch origin main
git pull origin main
fuser -k 3000/tcp
mdbook serve -n 0.0.0.0 -p 3000
