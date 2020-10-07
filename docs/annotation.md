# NL2SparQL4NLU Annotation Schema

## Intent Annotation
Intent labels are composed of 3 (4) parts

- ISO dialog act
    - `request`: search queries, etc.
    - `setq`: set question (WH)
    - `propq`: propositional question (YN)
- requested slot
- requested modality
    - `visual`
    - `auditory`
    - unspecified
- specification
    - `ref`: object of query is known, does not have entity in a query
    - `imp`: 'request' is implicit; e.g. NP query
    
intents:
- setq/movie.release_date
- setq/movie.release_date/ref

- propq/movie.release_date
- propq/movie.release_date/ref

- request/movie.release_date
- request/movie.release_date/imp
- request/movie.release_date/ref
- request/movie.release_date/imp+ref

- request/movie.release_date/visual
- request/movie.release_date/visual/ref

- request/movie.release_date/auditory
- request/movie.release_date/auditory/ref

## Entity Annotation