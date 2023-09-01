# Data
This folder contains all the original datasets provided by ementalhealth.ca we used in this project.

* Most-popular-search-terms.csv:
    * This file was selected from interactions on the mentalhealth.ca website and it contains the top 200 terms most frequently searched by users, a summary of high-frequency search terms helps us to conduct careful testing and refine the functionality of our virtual assistant. 

* infoSheets_2023-05-18.csv:
    * This file contains various mental illnesses and their descriptions, where "name_en" is the title of the info sheet; "abstract_en" is a short description (one or two sentences) that summarizes the info sheet, but not every info sheet has an abstract; "description_en" is the main body of the info sheet; and "taxonomy_heading_ids" is the list of headings that the info sheet is assigned to, but not every info sheet is assigned to a heading.

* map_records_under_heading.csv:
    * This file is an important bridge connecting the Records and Taxonomy_headings and can form an association. Leveraging parent-child relationships (where "parent_id" represents Taxonomy_headings and "child_id" represents Records), it can navigate complex links between these two key tables. Each heading can have one or more child records and each record can have one or more parent headings.

* records.json:
    * This file contains the name, description, age range of patients accepted, location, and languages spoken of a mental health resource of some kind that is dedicated to mental health treatment or aiding individuals dealing with mental health issues.

* taxonomy_headings.json:
    * This file represents mental health conditions and categories, such as depression, anxiety, art therapy, legal aid, etc. Records and Taxonomy_headings are mapped to indicate the kinds of mental health services the record provides. Moreover, a heading has one parent heading, and multiple child headings.
