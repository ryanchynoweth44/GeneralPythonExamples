# Coding Exercise

This coding execise is developed using python 3.8.3. 

## Set up

Requirements:  
- [Anaconda Installed](anaconda.org)
<br></br>

1. Clone or unzip the code repository, and open an Anaconda command prompt to the root of the project. 

1. Create an anaconda environment with the provided YAML file. 
    ```python
    conda env create -f environment.yml
    ```

1. Alternatively, you can create your own environment. 
    ```
    conda create -n trenv python=3.8.3 pytest -y
    ```

1. Activate your environment via the command line. 
    ```
    conda activate trenv
    ```

1. To run the pytests module, run the following:
    ```
    pytest test_run.py
    ```

1. To run the application execute the following command, and provide an input path, output path, and change file path. Please note that you must either use all default values (no arguments) or provide all three path values. By default we will use the following: 
    - input file: `data/tr_member_fav_drink.json`
    - change file: `data/tr_member_fav_drink_changes.json`
    - output file: `data/tr_member_fav_drink_updated.json`

    ```
    # with the defaults
    python run.py

    # with arguments
    python run.py <input file> <change file> <output file>

    # arg example
    python run.py data/tr_member_fav_drink.json data/tr_member_fav_drink_changes.json data/tr_member_fav_drink_updated.json
    ```

## Application Overview






## Change File Format

The change file format closely mirrors the given input file. The change file is a json file that contains three separate arrays for users, drinks, and favorite_tr_drinks. EAch array is expected to have the appropriate object structure. Please note that valid `actions` for all three types of objects are `add` and `delete`.  

For the user object we expect the following information. 
```json
{
    "action": "add",
    "name": "Ryan Chynoweth"
}
```

For the drinks object we expect the following information. 
```json
{
    "action": "add",
    "type": "Sparkling Ice",
    "flavor": "Kiwi"
}
```

For the favorite_tr_drinks object we expect the following information. 
```json
{
    "action": "add",
    "fav_drink": {
        "user_id": "3",
        "drinks": [
            {
                "type": "Sparkling Ice",
                "flavor": "Kiwi"
            },
            {
                "type": "New Type 1",
                "flavor": "New Flavor 1"
            }
        ]
    }
}
```




## Challenge Criteria

You can select the programming language of your choice to create a command line batch application which takes in an input file with a series of changes in order to generate an output.

Details:
1.	Input File (tr_member_fav_drink.json), this consists of user, drink and favorite_tr_drinks that are part of a marketing service
2.	Your application will take this file (tr_member_fav_drink.json) as input 
3.	Your application will also take a change file as input
4.	You can structure the change file the way you like
5.	The changes file should include multiple changes in one file
6.	You will code for the changes your application should support
7.	Your application will output "tr_member_fav_drink_updated.json" in the same structure as tr_member_fav_drink.json with the processed changes
8.	Sample: appname <inputfile> <changefile> <outputfile> 
 

The types of changes your application needs to support are:
1.	Add an existing drink to an existing favorite_tr_drinks
2.	Add a new favorite_tr_drinks for an existing user; the favorite_tr_drinks should contain at least one existing drink
3.	Remove an existing favorite_tr_drinks


