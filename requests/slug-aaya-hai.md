## Dekho, Dekho - Slug aaya hai!

Ab aap yeh link -
[http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=requests__using-json](http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug=requests__using-json)
open karein. Aise link ko use kar kar, aap kisi particular exercise ka content
nikal sakte hai.

Yeh karne ke liye teen steps honge:

1 - Sabse pehle aap user se input loge, ki user kaunsi exercise ka content dekhna chahta hai
2 - User se input lekar, aap corresponding exercise ka `slug` nikaloge
3 - Yeh `slug` aur purana `course_id` use kar kar, aap uppar wale jaisa URL call karoge

### Slug Nikalne ke liye hints
Pehle toh aap yeh samjhiye, slug nikalna normal programming hai,
iska requests se kuch khaas lena dena nahi hai.

Jaise hi user input karega, toh aap ko dekhna padega, ki woh parent
exercise hai, child exercise.

Phir aap yeh process repeat karna:

    - Aap kuch select karna, aur manually list mei se uski `slug` dhoondhna.
    - Yeh aap 5 se 10 baar karo.
    - Yeh karte karte observe karo, ki aap slug kaise nikal rahe ho.
    - Aap ussi karne ke tareeke ki - ek user story likho.
    - Uss user story ko code mei badalne ki koshish karo

Aise kar kar shayad aap soch pao, ki kaise user ki selection ke basis par aap usse
koi slug recommend kar sakte ho.