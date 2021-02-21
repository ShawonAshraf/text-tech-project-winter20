# Text Technology Project
Winter 2020-2021

IMS, Universität Stuttgart


## Setting up python env
Create a virtual env using the requirements.py file. Or if you are using Anaconda, create a conda env 
and then install from this file. 

```bash
# venv
python3 -m venv ./venv
# or python depending on your os
source venv/bin/activate
# check the appropriate command for windows
pip install -r requirements.txt

# for anaconda
conda create -n ttw python=3 -y
conda activate ttw
pip install -r requirements.txt
```

## Running code
The entrypoint here is `app.py`. It'll connect to the database and then you can call `DataFactory`
methods to fetch data. Use the methods for generating `XML` and validate them. Check the `generated` directory
for some generated and validated xml files.

__Always make sure to use the generated directory for storing generated xml files.__

## Directory Structure
- `/data` : contains the csv file
- `/db` : contains the sqlite database
- `/generated` : contains the generated xml
- `/view` : scripts for generating xml views
- `/schema` : contains the schemas to validate generated xml

## XML Schemas (XSD)
We have 5 different xml schemas that can be found in the /schema folder. They are:

1. TweetDataSchema.xsd, a schema for defining the Tweets.
2. HashTagSchema.xsd, a schema only for hashtags.
3. HashTagSchemaWithTweet.xsd, a schema for hashtags with the Tweets under the hasgtag.
4. LocationSchema.xsd, a schema only for user locations.
5. LocationSchemaWithTweet.xsd, a schema for user locations with the Tweets under the user location.
