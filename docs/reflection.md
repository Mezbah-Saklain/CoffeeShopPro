# Reflection Essay — CoffeeShopPro

**Word count: ~600**

## Technical Decisions

For CoffeeShopPro I chose the **Incremental** software development model. 
The project was constructed in three visible increments — the design-pattern core 
from Lab 2, then persistence and administration, then a tested and CI-integrated 
version. Each increment produced a working artifact I could demo, which mattered 
because I had roughly one day to complete the lab and could not afford a model 
where the product doesn't work until the end. I rejected Waterfall because 
requirements clarified as modules were added (the Admin module only made sense 
once persistence existed), and I rejected Agile/Scrum because sprint ceremonies 
are overkill for a solo project.

My biggest technical decision was **choosing GitHub Actions as the new 
self-learned tool**. I compared it with Jenkins (requires a dedicated server, 
plugins, and maintenance) and GitLab CI (would require migrating the repo away 
from GitHub). GitHub Actions won because it is free, hosted, and integrates 
natively with the repository I already used. I also chose to extend the existing 
Coffee Shop project rather than build a new web application; I am not strong in 
front-end development, and the design patterns from Lab 2 directly satisfied 
three of the lab's requirements. This let me spend my time on testing, CI, and 
the SDLC documentation rather than re-learning React.

## Challenges

The most demanding part was **testing with mocks**. My initial facade tests 
instantiated the real `Database`, which created a physical SQLite file — tests 
ran slowly and were order-dependent because state leaked between them. Reading 
the `unittest.mock` documentation, I learned to inject a `MagicMock()` through the 
Facade's constructor, so the test verified that `save_order` was called with the 
correct arguments while touching nothing on disk. Debugging `call_args` vs. 
`call_args_list` (I needed the former) took another 20 minutes.

Configuring `ci.yml` also caused failures. My first workflow ran Python 3.8, and 
my code uses 3.11 features — I discovered this only after reading the job logs. 
The second failure was a YAML indentation error caused by a stray tab. Both were 
quick fixes but both were real and instructive.

Resolving the merge conflict taught me that conflicts are not failures — they 
occur when two developers edit the same lines, and resolving them requires 
reading both versions carefully.

## Evaluation of My Learning Resources

The **official GitHub Actions documentation** was clear, accurate, and 
up-to-date; I would rate it 9/10. The **official Python documentation** on 
`unittest.mock` and `sqlite3` was authoritative and thorough (9/10). One 
**YouTube tutorial** was outdated (referenced `setup-python@v2` when v5 is 
current), which cost me a failed CI run; I rate it 5/10 for freshness. 
**Stack Overflow** resolved my "no such table" error in one search (8/10).

## Plan for the Next Skill

Based on this project, I want to learn **Docker** next. My CI pipeline runs 
tests on a GitHub-hosted VM, but I cannot easily reproduce that environment 
locally — a Docker container would let me run the exact same environment on my 
laptop. This would eliminate the class of "works on my machine" bug I nearly hit 
with Python versioning. After Docker, I want to learn **Selenium** for 
end-to-end UI testing, because my current tests only cover logic, not user 
interaction. My concrete plan is to spend two weeks on Docker fundamentals 
(Dockerfile, images, containers, volumes), then containerise CoffeeShopPro and 
extend `ci.yml` to build a Docker image.

## AI Tool Usage Statement

Portions of this project — specifically the initial code scaffold and the 
structural organization of test files — were generated with the assistance of an 
AI assistant. All code was run, debugged, and understood by me, and every 
component is defensible in the viva.