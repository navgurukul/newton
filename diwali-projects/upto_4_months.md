```ngMeta
name: Project for students who have joined within last 4 months
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
Aap ko better_exceptions project ko fork karna hai, aur isko ng_exceptions ke naam se plugin banana hai. Dekho code mei kaha kaha changes karne padenge to ensure ki ab plugin ka naam `ng_extensions` ho jaye.

Samajhne ke liye aisa socho, ki aapne aaj decide kiya aap ko aaj apna naam change karna hai. Iske liye aapko bahut saara kaam karna hoga - apna naam apni bank statement, apne friends mei, apne school mei, har jagah change karana hoga. Agar kahi par abhi aap ka poorana naam hai, toh woh error throw karega kyuki uski jagah ab naya naam hona chahiye tha.

### Using `ng_exceptions`
```bash
pip install -e <DIRECTORY>
```

Aise aap apne naye plugin ko install karein.
Jaise aapne `better-exceptions` use kiya tha, waise hi verify karein ki `ng-exceptions` bhi aap chala paa rahe hai.

## Step 2