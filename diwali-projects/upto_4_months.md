```ngMeta
name: Project for students who joined within last 6 months
completionMethod: manual
```

### HiPy

Iss project mei hum `python` ko seekhne mei hamari help karne ke liye hum ek extension banayenge.

### Using `better_exceptions`
[Iss module](https://github.com/Qix-/better-exceptions) ko install aur use karne ki instructions dekhein.
Jiss python shell mei better_exceptions enabled hai, waha par yeh code execute karne ki koshish karein:

```python
ek_sample_variable = 2

def error_wala_function( koi_bhi_argument ):
    return koi_bhi_argument * ek_undefined_variable

error_wala_function( ek_sample_variable )
```

Iss function ko normal python shell mei bhi execute kar kar dekhein, difference samajhne ke liye.

## Step 1
### Create a fork of this project
Aap ko better_exceptions project ko fork karna hai, aur isko ng_exceptions ke naam se plugin banana hai. Dekho code mei kaha kaha changes karne padenge to ensure ki ab plugin ka naam `ng-exceptions` ho jaye.

Samajhne ke liye aisa socho, ki aapne aaj decide kiya aap ko aaj apna naam change karna hai. Iske liye aapko bahut saara kaam karna hoga - apna naam apni bank statement, apne friends mei, apne school mei, har jagah change karana hoga. Agar kahi par abhi aap ka poorana naam hai, toh woh error throw karega kyuki uski jagah ab naya naam hona chahiye tha.

### Using `ng_exceptions`
```bash
pip install -e <DIRECTORY>
```

Aise aap apne naye plugin ko install karein.
Jaise aapne `better-exceptions` use kiya tha, waise hi verify karein ki `ng-exceptions` bhi aap chala paa rahe hai.

## Step 2
Ab aapko ek better_exceptions.py folder ke andar ek file create karni hai - `translate.py` ke naam se. Iss file ka kaam hoga ki jo bhi errors aati hai English mei, woh aapko Hindi mei print karni hai.

Aapko iss file ko aisa load karna hai ki aapka naya plugin `ng-exceptions` hindi mei user ko bataye, ki usne kya galti ki hai. Yeh kaise hai, sabse important step hai. Is ke liye aapko samajhna hoga ki `formatter.py` file kaise kaam kar rahi hai. `formatter.py` aur `__init__.py` files ko acche se padh kar samjho ki aap yeh kaise achieve kar sakte hai.

### Hai na useful? :)
#### Happy Coding!