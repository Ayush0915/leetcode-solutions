class Robot {
public:
    int w, h;
    int x, y; // current position
    int dir;
    int perimeter;

    Robot(int width, int height) {

        w = width;
        h = height;
        x = 0;
        y = 0;
        dir = 0;
        perimeter = 2 * (w + h) - 4; // total loop steps
    }

    void step(int num) {
        // to move forward num steps

         num %= perimeter; // still a doubt
         while(num>0)
         {
        if (dir == 0)         // east
        {
            int step = min(num, w - 1 - x);
            x += step;
            num -= step;
            if (step == 0)
                dir = 1;
        }
        else if(dir ==1) //north 
        {
            int step = min(num,h-1-y);
            y+=step;
            num-=step;

            if(step==0) dir=  2;
        }

        else if (dir ==2)//west
        {
            int step= min(num,x);
            x-=step;
            num-=step;

            if(step==0) dir = 3;
        }
        else // south
        {
            int step = min(num,y);
            y-=step;
            num-=step;

            if(step==0) dir=0;
        }
         }

        if(x==0&&y==0&&num==0)
        {
            dir = 3;//face south 
        }
    }

    vector<int> getPos() { return {x, y}; }

    string getDir() {
        if (dir == 0)
            return "East";
        if (dir == 1)
            return "North";
        if (dir == 2)
            return "West";
        return "South";
    }
};

/**
 * Your Robot object will be instantiated and called as such:
 * Robot* obj = new Robot(width, height);
 * obj->step(num);
 * vector<int> param_2 = obj->getPos();
 * string param_3 = obj->getDir();
 */
