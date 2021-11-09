Question3_key1
Question3_key2


Question3_key3


Question3_key4


Question3_key5


Question3_key6


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