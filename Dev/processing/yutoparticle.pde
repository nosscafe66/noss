//今編集しているプログラム
float VEL = 100.0;//最大加速
float ACC = 2.5;//最大加速度
ArrayList<Particle> particles;
ArrayList<Particle> particles2;
ArrayList<Particle> particles3;
PVector l = new PVector();
float x = random(0, width); 
float y = random(0, height); 
float speedX = 5; 
float speedY = 4; 
int time1 = 2500;
int time2 = 5000;
int time3 = 7500;
int time4 = 10000;
int time5 = 12500;
int time6 = 15000;
int time7 = 17500;
int h = 0 ;
int s = 100;
int b = 100;


import ddf.minim.*;
Minim minim;
AudioPlayer player;

void setup(){
  size(980, 730, P3D);
  
  particles3 = new ArrayList<Particle>();  
  for(int i = 0; i < 2000; i++)
  {
    particles3.add(new Particle());
  }
  minim = new Minim(this);
  player = minim.loadFile("Eternal Garden - Dan Henig.mp3");
  player.loop();
  smooth(4);
}


void draw(){
  background(250,250,250,5);
  lights();
  directionalLight(51, 102, 126, 0, -1, 0);
  translate(width/2, height/2,100);
  rotateX(frameCount*0.01);
  rotateY(frameCount*0.01);
  rotateZ(frameCount*0.01);

  for(Particle p: particles3)
  {
   int time = millis();
    if (time > time1)
    {
      p.display4();
      p.update3();
    }
    if (time > time2)
    {
      p.stop();
    }
    if (time > time3)
    {
      p.display4();
      p.update2();
    }
    if (time > time4)
    {
      p.display4();
      p.update2();
    }
    if (time > time5)
    {
      p.display3();
      p.update3();
    }
    if (time > time6)
    {
      p.stop();
    }
    if (time > time7)
    {
      p.update3();
      p.display4();
    }
  }
  //saveFrame("frames/####.png");
}

class Particle
{
  PVector pos, vel, acc,gravity,loc,sp,force;
  Particle()
  {
    float posSize = noise(800,800);
    float posAng1 = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float posAng2 = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));//map(sin(frameCount*0.01), -100, 100, 0, -100)
    float posX = posSize * sin(posAng1) * posAng2;
    float posY = posSize * posAng1 * posAng2; 
    float posZ = posSize * posAng1;
    pos = new PVector(posX, posY, posZ);
    float velSize = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));
    float velAng1 = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float velAng2 = random(map(sin(frameCount*0.1), -100, 100, 0, -1000));//map(sin(frameCount*0.1), -100, 100, 0, -1000)
    float velX = velSize * velAng1 * velAng1;
    float velY = velSize * velAng1 * velAng2;
    float velZ = velSize * velAng1;
    force = new PVector(12.0, 8.0);
    vel = new PVector(velX,velY,velZ);
    loc = new PVector(random(0, width ), random( 0, height ), random( -300, -700 ));//random(-width, width ), random( -height, height ), random( -100, -700 )
    pos = new PVector(random(0,width), random(0,height), random(-300, -700));
    sp = new PVector();
    acc = new PVector();
    gravity  = new PVector(0.005,0.005,0.005);//0.5,0.5,0.5
    acc = force.mult(ACC);
  } 

void update1()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector(mouseX,mouseY, 100);//random(map(sin(frameCount*0.01), -1, 1, 0, -1000))
    dir.sub(pos);
    dir.normalize();
    sp.add(dir);
    vel.add(acc);
    vel.limit(VEL*mix);
    pos.add(sp);
    vel.add(gravity);
    pos.add(sp);
}
  
void update2()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector(mouseX,mouseY, 100);//random(map(sin(frameCount*0.01), -1, 1, 0, -1000))
    dir.sub(pos);
    dir.normalize();
    sp.add(dir);
    //acc.limit(ACC*mix); //---
    vel.add(acc);
    vel.limit(VEL*mix);
    //pos.add(sp); //--
    vel.add(gravity);
    pos.add(sp);
}
  
void update3()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector(vel.x,vel.y,vel.z);
    dir.sub(pos);
    dir.normalize();
    acc.set(sp.x,sp.y,sp.z);
    sp.add(dir);
    acc.limit(ACC*mix);
    vel.add(acc);
    vel.limit(VEL*mix);
    pos.add(sp);
    vel.add(gravity);
    pos.add(sp);
}
  
void update()
{
    float mix = player.left.level() * width/100;
    PVector dir = new PVector( mouseX, mouseY, -500 );
    dir.sub( pos );
    dir.normalize();
    sp.add( dir );
    pos.add( sp );
}
  
void stop()
{
    sp.mult( .1 );
    sp.add(gravity);
    sp.add(acc);
}
void display1()
{
    float mix = player.left.level() * width/50;
    pushMatrix();
    rotateToFace(pos);//240,200,220,5
    translate(-pos.x, pos.y, -pos.z);
    fill(50,200,250,100);
    ellipse(pos.x+mix, pos.y+mix, ACC, ACC);
    translate(pos.x, pos.y, pos.z);
    fill(250,200,200,200);
    ellipse(-pos.x+mix, -pos.y+mix, ACC, ACC);
    translate(loc.x, -loc.y, loc.z);
    fill(250,250,250,200);
    ellipse(-pos.x+mix, -pos.y+mix, ACC, ACC);
    popMatrix();
}
void display2()
{
    float mix = player.left.level() * width/100;
    pushMatrix();
    rotateToFace(pos);
    translate(-pos.x, pos.y, -pos.z);
    stroke(255+pos.x,189+pos.y,189+pos.z,250);
    fill(255+pos.x,189+pos.y,189+pos.z,250);
    ellipse(pos.x+mix, pos.y, ACC, ACC);
    popMatrix();
}
void display3()
{
    int time = millis();
    float mix = player.left.level() * width/200;
    pushMatrix();
    rotateToFace(pos);
    translate(-pos.x, pos.y, -pos.z);
    stroke(pos.x,139+pos.y,10+pos.z,250);
    fill(pos.x,139+pos.y,10+pos.z,250);
    ellipse(pos.x+mix, pos.y, ACC, ACC); 
    popMatrix();
}
void display4()
{
    int time = millis();
    float mix = player.left.level() * width/200;
    pushMatrix();
    rotateToFace(pos);
    fill(0,0,0,200);
    stroke(0,0,0,250);
    ellipse(pos.x, -pos.y, ACC, ACC);
    popMatrix();
}
PVector U = new PVector(100,100,100);
void rotateToFace( PVector P )
{
    PVector D = new PVector();
    D.set(l);
    D.sub(P);
    PVector r = U.cross( D );
    r.normalize();
    PVector Backwards = r.cross( U );
    Backwards.normalize();
    PVector rUp = Backwards.cross(r);
    applyMatrix(r.z, r.x, r.y, 0, rUp.x, rUp.y, rUp.z, 0, Backwards.x, Backwards.y, Backwards.z, 0, 0, 0, 0, 1);
 }
}
