
sync:
	git pull
	git status
	git add . 
	git commit -a -m "Sync changes"
	git push
	git status


### ------------
# Pyton
### ------------
py-venv:
	python -m venv .venv
	 .\.venv\Scripts\activate
