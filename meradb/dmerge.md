## DMerge -> dmerge('some_other.db')

Iss function ko banane ke liye
- aap current database mei, `dmerge` naam ka function define karoge
- `dmerge` ek doosre database ka naam doge
- Current database mei aapko, naya wala database jo argument diya hai, woh load karna hai
  - Iske liye Aap existing class ke andar khud ka ek naya object bana sakte ho
- Phir uss database ki saari `keys` aur unki corresponding `values` apne existing `database` mei add karo