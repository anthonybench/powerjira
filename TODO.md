## Hot
- advertize usage in readme
- parameterize `ticket_excerpt_length`
- `[list, done]` in the `watched` command should likely be `[list, prune]`
- implement ticket closing (`pj close` marks as done) 
    - delete (`--delete`)
- guard against invalid init status, so it exists before it makes the ticket
- `pj watched list` is broken "The requested API has been removed"
- `pj fetch "in progress` returns nothing


## Cold
- github action for pypi build
- support different editors
- show username instead of user-id for ticket dry runs
- implement logging