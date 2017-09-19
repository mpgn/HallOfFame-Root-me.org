# HallOfFame Root-me

Hall Of Fame dashboard for Root-me.org. Users information are in the `users.json`.

![screenshot](https://i.gyazo.com/56b4c6fcc5c5306e3d904735c0716835.png)

## Informations

Since root-me doesn't have any API, this is dirty parsing ! But it's working ;)

/!\ The statistics in the demo are not updated every night !

### Add/Update a user

Add the user in the `users.json` like this :
```
python update.py username realname
```
You can get the useranme form the url of a Root-me profile : https://www.root-me.org/username 
**/!\ CAUTION: take the username from the URL !**

Update the json like this : 
```
python3 update.py update
```

Use a cron job to update the script every night ;)

Delete username : 
```
python3 update.py delete username
```

## History

* 0.0.1
	* First release
* 0.0.2
	* Fix issues
* 0.0.2
	* Add delete function

## Credits

* [@mpgn_x64](https://twitter.com/mpgn_x64)

## License

MIT License
