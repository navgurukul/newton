```js
const result = {
   success: ["max-length", "no-amd" “prefer-arrow-functions”],
   failure: ["no-var", "var-on-top", "linebreak"]:
   skipped: ["no-extra-semi", "no-dup-keys"]
 };


Output should be
max-length
no-amd
prefer-arrow-functions
 
const success=result.success
const store=success,length
for(const value in success){
  console.log(store[value])
}

```