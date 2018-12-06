BUILD
=====
Copy swagger.json from https://api.thetvdb.com/swagger.json to local swagger.json

Run the following command to generate the code based on the tvdbapi v2 swagger.json:

    swagger-codegen-cli-2.2.3.jar generate -i https://api.thetvdb.com/swagger.json -l python -c config.json -o ..