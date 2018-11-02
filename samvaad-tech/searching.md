```ngMeta
name: Searching
completionMethod: manual
```
## What is Searching
A search is a that where find or searching any data, roll number, and type information from list.
That is called search.

## There are two type of search.
 1) Linear Search
 2) Binary Search

## Linear searching :--
 Linear search is a searching any data by sequence or series.that is call Linear searching.

Example:--
a= array
n= number of elements
x= which number you want to search
	     1	      2	      3   	     4	     5	     6	
4
8
6
12
15
3


Linear search(a,n,x)
For i=a to n;(using for loop)
If a[i]==x;
    Return i;
Return 0; (there is no element which you want to search)

## Searching ko aur samjne ke liye aap ye video dekh skte hai

@[youtube](U55MOdjEWKY)

## Advatages of Linear Search
1) It is very easy to understand and implement;
2) It does not require the data in the array to be stored in any particular order.

## Binary Searching
Binary search works on sorted arrays. Binary search begins by comparing the middle element of the array with the target value. If the target value matches the middle element, its position in the array is returned. If the target value is less than the middle element, the search continues in the lower half of the array.
syntax:--
Find the location of value
 
  	      0	     1	      2   	     3	     4	     5	
<table>
	<tr><td>10</td>
	<td>18</td>
	<td>19</td>
	<td>21</td>
	<td>23</td>
	<td>25</td></tr>		
	
</table>

While low<=high<br>
Do mid=(low+high)/2<br>
If v=a[mid]<br>
    Return mid<br>
If v>a[mid]<br>
low=mid+1<br>
Else high =mid +1<br>
Return nill<br> 

## Binary Searching ko detail main samjne ke liye ye video dekhe

@[youtube](1HIFzve0zCM)

## About detail of Binary search:

https://en.wikipedia.org/wiki/Binary_search_algorithm.<br>

## Advantages of Binary search:-
 1) If the array being searched contains 20,000 elements, the algorithm will have to look at all 20,000 elements in order to find a value in the last element.
 2) The binary search is much more efficient than the linear search.

Ab aapko 30 mins ke liye aapas mei english mei inn topics ke baarein mei baat karni hai.
Baat karte karte, aap observe karein, ki aap kitne tech words use kar paa rahe hai.

##Aur agar aapka partner koi aisa tech word bolta hai, jo aapko nahi pata, ya aap generally use nahi kartein. Inn words ko bhi samajhne ki phir koshish karein

Iss discussion ko karte hue, aap inn points ke baarein mei bhi soch sakte hai:

1.Search Engine Kya hai?<br>
2.Kitne types ke Search Engine hote hai?
