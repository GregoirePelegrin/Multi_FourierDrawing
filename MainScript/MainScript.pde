FloatList initAngleList;
FloatList sizeList;
FloatList speedList;
ArrayList<Circle> circles;
Circle lastCircle;
int nbrCircles;
ArrayList<FloatList> drawing;

void setup(){
  fullScreen();
  frameRate(30);
  
  initAngleList = new FloatList();
  sizeList = new FloatList();
  speedList = new FloatList();
  circles = new ArrayList<Circle>();
  nbrCircles = 10;
  drawing = new ArrayList<FloatList>();
  
  for(int i = 0; i<nbrCircles; i++){
    // Positive frequency
    initAngleList.append(i * PI/nbrCircles);
    sizeList.append(100 * (nbrCircles-i)/nbrCircles);
    speedList.append(map(i, 0, nbrCircles, PI/960, PI/240));
    // Negative frequency
    initAngleList.append(i * PI/nbrCircles);
    sizeList.append(100 * (nbrCircles-i)/nbrCircles);
    speedList.append(- map(i, 0, nbrCircles, PI/960, PI/240));
  }
  
  Circle circle = new Circle(speedList.get(0), sizeList.get(0), initAngleList.get(0));
  circle.setFirst();
  circles.add(circle);
  for(int i = 1; i<nbrCircles*2; i++){
    circle = new Circle(speedList.get(i), sizeList.get(i), initAngleList.get(i));
    circles.get(i-1).setNext(circle);
    circle.setPrecedent(circles.get(i-1));
    circles.add(circle);
    lastCircle = circle;
  }
}

void draw(){
  background(0);
  translate(width/2, height/2);
  noFill();
  
  if(drawing.size() > 5000){
    drawing.remove(0);
  }
  beginShape();
  for(FloatList coord : drawing){
    vertex(coord.get(0), coord.get(1));
  }
  endShape();
  
  for(Circle circle : circles){
    circle.update();
  }
  lastCircle.display();
  
  drawing.add(getPoint());
}

FloatList getPoint(){
  FloatList coord = new FloatList();
  float xCoord = 0;
  float yCoord = 0;
  
  Circle currentCircle = circles.get(0);
  while(currentCircle.hasNext){
    xCoord += currentCircle.size * cos(currentCircle.angle);
    yCoord += currentCircle.size * sin(currentCircle.angle);
    currentCircle = currentCircle.next;
  }
  xCoord += currentCircle.size * cos(currentCircle.angle);
  yCoord += currentCircle.size * sin(currentCircle.angle);
  
  coord.append(xCoord);
  coord.append(yCoord);
  return coord;
}
