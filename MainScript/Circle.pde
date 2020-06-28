class Circle{
  Circle precedent;
  Circle next;
  boolean first;
  boolean hasAnterior;
  boolean hasNext;
  float speed;
  float size;
  float angle;
  
  Circle(float sp, float si, float a){
    this.first = false;
    this.hasAnterior = false;
    this.hasNext = false;
    this.speed = sp;
    this.size = si;
    this.angle = a;
  }
  
  void setPrecedent(Circle c){
    this.precedent = c;
    this.hasAnterior = true;
  }
  
  void setNext(Circle c){
    this.next = c;
    this.hasNext = true;
  }
  
  void setFirst(){
    this.first = true;
  }
  
  void update(){
    //this.angle += this.speed*2*PI;
    this.angle += this.speed*2*PI*1/480;
  }
  
  void display(){
    if(!this.first){
      this.precedent.display();
    }
    
    rotate(this.angle);
    stroke(255, 10);
    ellipse(0, 0, 2*this.size, 2*this.size);
    stroke(255, 50);
    line(0, 0, 2.0/3*this.size, 0);
    triangle(this.size, 0, 2.0/3*this.size, 1.0/6*this.size, 2.0/3*this.size, -1.0/6*this.size);
    translate(this.size, 0);
    rotate(-this.angle);
  }
}
