FloatList initAngleList;
FloatList sizeList;
FloatList speedList;
ArrayList<Circle> circles;
Circle lastCircle;
int nbrCircles;
ArrayList<FloatList> drawing;

void setup(){
  size(600, 600);
  frameRate(30);
  
  initAngleList = new FloatList();
  sizeList = new FloatList();
  speedList = new FloatList();
  circles = new ArrayList<Circle>();
  nbrCircles = 10;
  drawing = new ArrayList<FloatList>();
  
  for(int i = 0; i<nbrCircles; i++){
    initAngleList.append(i * PI/nbrCircles);
    sizeList.append(100 * (nbrCircles-i)/nbrCircles);
    speedList.append(map(i, 0, nbrCircles, PI/960, PI/240));
  }
  
  Circle circle = new Circle(speedList.get(0), sizeList.get(0), initAngleList.get(0));
  circle.setFirst();
  circles.add(circle);
  for(int i = 1; i<nbrCircles; i++){
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
  
  if(drawing.size() > 500){
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
  
  FloatList coord = new FloatList();
  float totalAngle = 0;
  float xCoord = 0;
  float yCoord = 0;
  Circle currentCircle = circles.get(0);
  while(currentCircle.hasNext){
    totalAngle += currentCircle.angle;
    xCoord += currentCircle.size * cos(totalAngle);
    yCoord += currentCircle.size * sin(totalAngle);
    currentCircle = currentCircle.next;
  }
  totalAngle += currentCircle.angle;
  xCoord += currentCircle.size * cos(totalAngle);
  yCoord += currentCircle.size * sin(totalAngle);
  coord.append(xCoord);
  coord.append(yCoord);
  drawing.add(coord);
}
