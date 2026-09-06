mkdir -p project/{scripts,data,docs}
touch project/scripts/{preprocessing,analysis,visualization}.py
touch project/data/{raw_data,processed_data}.csv
touch project/docs/{readme.txt,notes.txt}
ls -alh project
rm -rf project
