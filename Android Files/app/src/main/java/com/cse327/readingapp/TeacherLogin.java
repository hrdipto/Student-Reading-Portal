package com.cse327.readingapp;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.app.ProgressDialog;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;

public class TeacherLogin extends AppCompatActivity {

    private EditText emailt;
    private EditText passt;
    private Button loginBtn;
    private TextView registerText;
    private FirebaseAuth firebaseAuth;
    private ProgressDialog progressDialog;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_teacher_login);

        emailt = (EditText) findViewById(R.id.emailt);
        passt = (EditText) findViewById(R.id.passt);
        loginBtn = (Button) findViewById(R.id.loginBtn);
        registerText = (TextView) findViewById(R.id.registerText);

        firebaseAuth = FirebaseAuth.getInstance();
        progressDialog = new ProgressDialog(this);

//        FirebaseUser user = firebaseAuth.getCurrentUser();
//
//        if(user != null) {
//            finish();
//            startActivity(new Intent(StudentLogin.this, StudentProfile.class));
//        }

        loginBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String userEmail = emailt.getText().toString();
                String userPass = passt.getText().toString();

                if( userEmail.isEmpty() || userPass.isEmpty() ) {
                    Toast.makeText(TeacherLogin.this, "Please fill up the fields.", Toast.LENGTH_SHORT).show();
                } else {
                    validate(emailt.getText().toString(), passt.getText().toString());
                }
            }
        });

        registerText.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                startActivity(new Intent(TeacherLogin.this, TeacherRegister.class));
            }
        });
    }

    private void validate(String username, String password) {

        progressDialog.setMessage("Please wait");
        progressDialog.show();

        firebaseAuth.signInWithEmailAndPassword(username, password).addOnCompleteListener(new OnCompleteListener<AuthResult>() {
            @Override
            public void onComplete(@NonNull Task<AuthResult> task) {
                if (task.isSuccessful()){
                    progressDialog.dismiss();
                    Toast.makeText(TeacherLogin.this, "Login Successful", Toast.LENGTH_SHORT).show();
                    startActivity(new Intent(TeacherLogin.this, TeacherProfile.class));
                } else {
                    progressDialog.dismiss();
                    Toast.makeText(TeacherLogin.this, "Login Failed", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }
}
