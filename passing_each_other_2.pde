//変数宣言
int[] agent1 =new int[2];  //agent1はx,y座標を持っている
int[] agent2 =new int[2];  //agent2はx,y座標を持っている
int agent_x =10;
int agent_y =10;


int[] blf =new int[50] ; //ブロックの数
int blw =10;
int blh =10;
int delete_b =0;
int before=0;
int agent_num=0;

int count_collision_time =0;  //エージェント同士
boolean collision ; //衝突しそうになったか判定する変数
boolean space ; //空きスペースに入るのか判定する変数
boolean stop; //停止させるか判定する変数
boolean temp =false;
boolean once =false;
int block_delete;
int stop_time; //停止時間
int count_collision;  //空きスペースに入って衝突回避を行った回数


void blockDisp() {
  for (int i=0; i<blf.length; i++) {
    blf[i] =1;  //0:ブロック非表示 1:ブロック表示
  }
  for (int i=blf.length-1; i >=0; i--) {

    if (blf[i] ==1) {
      fill(255, 255, 255);
      blockHitCheck();

      rect((i%50) *(blw+2), 80, blw, blh, 2);    //上のブロック
    }
    rect((i%50) *(blw+2), 110, blw, blh, 2);    //下のブロック
  }
}

//ブロックとエージェントの当たり判定
void blockHitCheck() {

  if (agent2[1] !=100) {
    before =agent2[0]/12;
  }

  if (before !=0 ) {
    blf[before] =0;
  }
}

//エージェント１ or 2のどっちが空きスペースに入るか判定する関数
int agent_or_space () {
  //int agent1_near_b, agent2_near_b;
  //println(agent1[0]);
  //blockHitCheck();
  //agent1_near_b =agent1[0];
  //agent2_near_b =agent2[0];
  //println((agent1[0]/12) *12);
  //println("---------");
  //println(agent1[0]);
  if (((agent1[0]) -((agent1[0]/12) *12) + blw/2) < ((agent2[0] ) - ((agent2[0]/12) *12) + blw/2 )) {
    return 1;
  } else {
    return 2;
  }
}

void agent_move() {
  if (stop_time  >=250) {
    agent1[0] +=1;
  }


  //agent1[0] +=1;
  ellipse(agent1[0], agent1[1], agent_x, agent_y);  //エージェント1

  ellipse(agent2[0], agent2[1], agent_x, agent_y);  //エージェント2

  //もしエージェント１と2が衝突しそうになったらエージェント2が空きスペースに入る
  if (agent2[0] - agent1[0] <15  ) {

    if (once ==false) {
      agent_num = agent_or_space();
      once =true;
      //println(agent_num);
    }
    //println(agent_num);
    if (count_collision ==0) {
      collision =true;
    }
  }

  if (collision ==false) {
    agent2[0] -=1;
  } else if (collision ==true) {
    if (space ==false ) {
      if (agent_num ==1) {
        agent1[1] -=1;
      } else {
        agent2[1] -=1;
      }
      if (agent2[1] ==85 || agent1[1] ==85 ) {
        space =true;
      }
    } else if (space ==true) {
      if (agent_num ==1) {
        agent1[1] +=1;
       
      } else {
        agent2[1] +=1;
      }
      if (agent2[1] ==100) {
        collision =false;
        space =false;
        count_collision++;
      }
    }
  }
  stop_time +=1;
}

void setup() {
  //初期設定
  size(500, 500);
  agent1[0] =100; //agent1のx座標の初期位置
  agent1[1] =100; //agent1のy座標の初期位置
  agent2[0] =400; //agent2のx座標の初期位置
  agent2[1] =100; //agent2のy座標の初期位置
  count_collision_time =0; //衝突回数時間
  count_collision =0; //衝突回数
  stop_time=0;
  before=0;
  collision =false; //衝突していない
  space =false; //空きスペースに入っていない
  stop =false;
}

void draw() {
  background(0); //背景を黒にする
  blockDisp();    //ブロックの表示

  agent_move();  //エージェントを動かす
}
