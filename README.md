# Remarcable Take Home Assignemnt - Alex Bepple

## Assumptions
- The person attempting to run this has docker or podman set up to handle docker commands, and is running the Deamon
- The person attempting to run this code has downloaded the code/ cloned the repository


## Setup Instructions
1. Run ```docker compose up``` in the terminal at the base of the project
2. navigate to `0.0.0.0:8000/admin` and login with default credentials U: `admin` P:`Password123` 
3. Navigate to the `Categories` subsection in the catalog, and click button `SEED SAMPLE DATA`
4. Navigate to home page via url `0.0.0.0:8000` or clicking the `View Site` link at top of admin page


## Some nerdy talk about the considerations that went into the project.
### Backend
I went with the decision to have `categories` be a `one to many`, and `tags` be a `many to many` relation.

I also decided that `deleting a category` shouldnt delete the products in a category it should just `orphan the products`, and that would be okay.

I added endpoints to get each the tags, categories, and products so they may be selected separately. First load gets them all and caches them to be delt with on front end. 

`Products` are `Paginated` so it doesnt slam them all in on first load. If your screen is big enough it loads 2 chunks and gets them all, but the thought is there for scalability


### FrontEnd
one to many `category` meant some sort of dropdown, accordian, tab structure. I went with `dropdown`.

`Tags` made more sense to me to be `ors instead of ands` so adding more tags gave you more. Maybe thats a decision based on the 20 product lineup and a scaled system with more products you'd want different behaviour, but I'm happy with how it feels here.

Added a `selection functionality` to the program so that theres a reason to `search for something, clear filters, and search some more`.

Added some reactivity so smaller screens got some love too.

Figured using `ai` to bring in some `SVGS` and some splashes of `animation` in transitions would be good 

I tried to thematically fit into the product space of Remarcable by using examples from the construction contractor financial space. Hope you appreciate :D


### I might be foregetting some things, happy to answer questions.



## AI Attribution:
- Categories, Tags, and Products to add for the seed script. It came up with the 35 and the combinations.
- Conferred with it for documentation on some front end DOM and JS things that I was rusty on
- Helped accelerate coding based on the design choices I set out. 
