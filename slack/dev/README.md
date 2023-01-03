Slack Addon
===============

Deployment:
----------
Content of addon repo must be prepared for proper deployment to the server.
Currently it is a manual process consisting of steps: (requirements: at least Python3.8)
- clone repo to local machine
- run `python create_package.py` - this will produce `package` folder in root of cloned repo
- copy content of `package` folder to server machine to `openpype4-backend/addons` folder
  - example (current directory is root of cloned repo)
      - `cp -r package/slack SERVER_ROOT/openpype4-backend/addons`

Addon allowing sending notification to Slack channel(s) at the end of publishing.

It allows to upload thumbnail and review(for example mp4/mov) to the channel.
Uploading is limited by configurable file size to spare Slack disk limit.