## It's me - API - again ;)

Ab aap yeh link - [http://saral.navgurukul.org/api/courses/74/exercises](http://saral.navgurukul.org/api/courses/74/exercises)
open karein. Iss link mei, iss particular course ki saari
exercises ki list hai. Aur `slug`, `parentExerciseId`, `githubLink` jaisi
kuch aur bhi information hai. Iss information ko bhi hum aage use karenge.

Jo `course_id` user ne select ki hai, uske corresponding aapko yeh API
call karni hai. Phir jab aap yeh API call kar lenge, toh aapko kuch
uss tarah ka data milega jaisa uppar wale link se mila tha. Ab aapko
yeh exercise print karni hai terminal par. Kuch baatein jo important hai:

1 - Agar `childExercises` hai kisi bhi exercise ki toh, unko bhi print karni
hai. Kyuki woh childExercise hai, toh woh thoda sa side mei print karo, spaces
dekara. Unki numbering ke liye, socho kaise kar sakte ho.

2 - Jaise aapne pehle `id` nikali thi, user_choice ke vajah se, aise hi iss baar bhi
aapko, exercise ka `slug` nikal kar rakhna hai. Toh aapki numbering aisa karna, ki
jo user input karein, usse aap guess kar payo, ki kaunsi `exercise` user ne select ki
hai, aur uska corresponding `slug` kya hai.

3 - Jab bhi `parentExerciseId` null hoga json mei, toh `json.loads` function usse `Non
ki tarah read karega, and jab `childExercises`, khaali list hoga, toh [] ki tarah hi
python mei `json.loads` function aapko return karega.

## Debug Mei Help Ke Liye
Debug mei help karne ke liye, jab bhi aap yeh wala endpoint call karein, toh aap
apna result exercises_`id`.json mei save kar le. Jaise agar aapne course_id 74,
ke liye endpoint call kiya hai to uska reply - exercises_74.json mei save kar le.

Kisi bhi `course_id` ke liye API call karne se pehle dekhe ki uski corresponding
exercises_`id`.json file exist karti hai ya nahi. Agar karti hai, toh ussi file
ko read kar le, nahi toh API call kar kar, uss file ko create kar le.

Isse jab aap baar baar, yeh code run karoge, toh API requests nahi hongi, aur
aap aasaani se debug kar paoge.

## Bonus
Iss cheez ko caching bolte hai. Ek `debug` naam ka variable banao. Jab `debug`
ho toh hi, uppar wala behavior ho. Otherwise, jab `debug=False` set ho toh
hamesha API calls karo, chahe files exist karti ho ya nahi.