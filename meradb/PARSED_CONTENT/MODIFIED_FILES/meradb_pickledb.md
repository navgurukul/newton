## pickledb_key1
pickledb_key2

pickledb_key3[pickledb_key4](https://pythonhosted.org/pickleDB/)
pickledb_key5

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
pickledb_key6`load`pickledb_key7`set`pickledb_key8`get`pickledb_key9`dump`pickledb_key10

```bash
# For Python 2.7
sudo apt install python-pip
pip install pickledb

# For Python 3.0+
sudo apt install python3-pip
pip3 install pickledb
```
`pickledb`pickledb_key11