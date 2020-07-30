# Registrasi

## url & payload
```
http://192.168.1.3:3000/Register
```
```
{
	"user_video" :, // base64 without data/type header
	"client_id" : // region
}
```

## response

if path video doesn't exists
```
{
	"status" : "1"
}
```
```
else (success)
{
	"status" : "0", 
	"user_id_rkb" : string // random generated 16 digit number, `nnnn-nnnn-nnnn-nnnn`
}
```

# Recognize Image

## url & payload
```
http://192.168.1.3:3000/InferencingImage
```
```
{
	"user_image" : , // base64 string, without data/type header
	"client_id" : // region
}
```
## response

if face not found or failed in alignment face
```
{
	"status" : "1"
}
```
elif client id not valid or still on training (database doesn't exists)
```
{ 
	"status" : "2" 
}
```
elif path image doesn't exists
```
{ 
	"status" : "3" 
}
```
else, for every faces returned, put inside `"result"`
```
{
	"result": [ 
		"status" : "0", 
		"user_id_rkb" : string // random generated 16 digit number, `nnnn-nnnn-nnnn-nnnn`
		"confidence_level" : str(confidence_level) // float between 0.0 to 1.0
	]
}
```