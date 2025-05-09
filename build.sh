#!/bin/sh
cd ./my-tailwind-site/
npm run build
cp -r * ../webserver/
cd ../webserver
python app.py
