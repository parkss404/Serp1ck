package com.example.a1try.result;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.annotation.Nullable;
import androidx.appcompat.app.AppCompatActivity;

import com.example.a1try.MainActivity;
import com.example.a1try.R;

import java.util.Random;

public class XXXResult extends AppCompatActivity {

    private Button btn_222;
    private Button btn_end8;

    @Override
    protected void onCreate(@Nullable Bundle saveInstanceState) {
        super.onCreate(saveInstanceState);
        setContentView(R.layout.activity_result222);

        TextView XXX=findViewById(R.id.XXX);
        btn_222=findViewById(R.id.btn_222);
        btn_end8=findViewById(R.id.btn_end8);

        String[] XXXtxt=getResources().getStringArray(R.array.XXXtxt);
        Random random=new Random();
        int n= random.nextInt(XXXtxt.length-1);

        XXX.setText(XXXtxt[n]);

        btn_222.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String[] XXXtxt=getResources().getStringArray(R.array.XXXtxt);
                Random random=new Random();
                int n= random.nextInt(XXXtxt.length);

                XXX.setText(XXXtxt[n]);
            }
        });

        btn_end8.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v) {
                Intent intent =new Intent(XXXResult.this, MainActivity.class);
                startActivity(intent);
            }
        });
    }
}
