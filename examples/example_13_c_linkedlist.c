/* C: linked list example */
#include <stdio.h>
#include <stdlib.h>

struct Node{int v; struct Node*next;};

struct Node* add(struct Node*h,int v){
  struct Node*n=malloc(sizeof(*n));
  n->v=v; n->next=h;
  return n;
}

int main(){
  struct Node*h=NULL;
  h=add(h,1); h=add(h,2); h=add(h,3);
  for(struct Node*c=h;c;c=c->next) printf("%d ",c->v);
}
