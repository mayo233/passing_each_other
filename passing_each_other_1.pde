//変数宣言
int[] agent1 =new int[2];  //agent1はx,y座標を持っている
int[] agent2 =new int[2];  //agent2はx,y座標を持っている
int block ; //ブロックの数
int count_collision_time =0;  //エージェント同士
boolean collision ; //衝突しそうになったか判定する変数
boolean space ; //空きスペースに入るのか判定する変数
boolean stop; //停止させるか判定する変数
//boolean block_delete ; //ブロックが消える変数

int stop_time; //停止時間

int[] block_pos =new int[31]; //置かれているブロックの座標値

void agent_move() {  
  agent1[0] +=1;
  ellipse(agent1[0], agent1[1], 10, 10);  //エージェント1

  ellipse(agent2[0], agent2[1], 10, 10);  //エージェント2

  //もしエージェント１と2が衝突しそうになったらエージェント2が空きスペースに入る
  if (agent2[0] - agent1[0] <15) {
    if (count_collision_time ==0) {
      collision =true;
    }
  }

  if (collision ==false) {
    agent2[0] -=1;
  } else if (collision ==true) {
    if (space ==false) {
      agent2[1] -=1;
      if (agent2[1] ==85) {
        space =true;
      }
    } else if (space ==true) {
      agent2[1] +=1;
      if (agent2[1] ==100) {
        collision =false;
        space =false;
        
      }
    }
    count_collision_time ++;
    //println(count_collision_time);
  }
}

void setup() {
  //初期設定
  size(500, 500);
  agent1[0] =100; //agent1のx座標の初期位置
  agent1[1] =100; //agent1のy座標の初期位置
  agent2[0] =400; //agent2のx座標の初期位置
  agent2[1] =100; //agent2のy座標の初期位置
  block=31;  //置かれているブロックの個数
  count_collision_time =0; //衝突回数
  stop_time=0;
  collision =false; //衝突していない
  space =false; //空きスペースに入っていない
  stop =false;
}

void draw() {
  background(0); //背景を黒にする
  //ブロックを置く
  for (int i=0; i<block; i++) {
    rect(90+i*10, 110, 10, 10); //下の壁
    block_pos[i] =90+i*10;

    //16個目のブロックを消す
    if (i ==16) {
      continue;
    }
    rect(90+i*10, 80, 10, 10);  //上の壁
  }

  agent_move();  //エージェントを動かす
}
