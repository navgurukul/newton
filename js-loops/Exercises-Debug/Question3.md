Output should be 

max-length
no-amd
prefer-arrow-functions

```javascript
const result = {
   success: ["max-length", "no-amd" “prefer-arrow-functions”],
   failure: ["no-var", "var-on-top", "linebreak"]:
   skipped: ["no-extra-semi", "no-dup-keys"]
 };


const success=result.success
const store=success,length
for(const value in success){
  console.log(store[value])
}
```


```solution
const result = {
   success: ["max-length", "no-amd" ,"prefer-arrow-functions"],
   failure: ["no-var", "var-on-top", "linebreak"],
   skipped: ["no-extra-semi", "no-dup-keys"]
 };
 
const success=result.success
const store=success.length
for(const value in success){
   console.log(success[value]);
}
```

For the next course [clickHere](https://www.merakilearn.org/course/126/exercise/3256)
