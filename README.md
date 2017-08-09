# HallOfFame

Hall Of Fame dashboard  for Root-me.org. All users are manually added to the file `users.json`, then with a cron job, the script `update.py` do the rest.

![screenshot](https://i.gyazo.com/1823b9244ef0c4c98d5877f837880dda.png)

## Informations

Since root-me doesn't have any API, this is dirty parsing ! But it's working ;)

### Add/Update a user

Add the user in the `users.json` like this :
```
python update.py 'username' 'realname'
```

Update the json like this :
```
python3 update.py
```

Use a cron job to update the script every night ;)

## History

* 0.0.1
	* First release

## Credits

* [@mpgn_x64](https://twitter.com/mpgn_x64)

## License

MIT License
