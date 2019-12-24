BUILD
=====
Copy swagger.json from https://api.thetvdb.com/swagger.json to local swagger.json

Run the following command to generate the code based on the tvdbapi swagger.json:

    swagger-codegen-cli-2.4.10.jar generate -i https://api.thetvdb.com/swagger.json -l python -c config.json -o ..