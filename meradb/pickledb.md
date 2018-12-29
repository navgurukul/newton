## Pickle DB

Iss exercise mei humei ek bahut sa simple sa database banana hai.

Yeh [padhein](https://pythonhosted.org/pickleDB/). Aise databases ko key-value store ya key-value database bolte hai. Kyuki - yeh database aapko kisi bhi key ke liye uske corresponding values return karte hai.

```bash
>>> import pickledb

>>> db = pickledb.load('example.db', False)

>>> db.set('key', 'value')
True

>>> db.get('key')
'value'

>>> db.dump()
True
```

Uss link par aapne yeh code padha hoga. Humein - sabse pehle yeh chaar commands implement karni hai - `load`, `set`, `get` and `dump`. Sabse pehle aap -

```bash
# For Python 2.7
sudo apt install python-pip
pip install pickledb

# For Python 3.0+
sudo apt install python3-pip
pip3 install pickledb
```

`pickledb` khel kar, usmei kuch values insert karo, kuch values read karo, database dump kar kar file ke content dekho, etc. Aap ne kya kya commands try ki, neeche comment box mei likhiye.