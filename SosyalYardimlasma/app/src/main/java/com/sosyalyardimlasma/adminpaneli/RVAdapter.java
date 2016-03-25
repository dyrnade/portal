package com.sosyalyardimlasma.adminpaneli;

import android.app.AlertDialog;
import android.content.Context;
import android.content.DialogInterface;
import android.support.v7.widget.CardView;
import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import com.sosyalyardimlasma.adminpaneli.R;

import java.util.ArrayList;

public class RVAdapter extends RecyclerView.Adapter<RVAdapter.MaterialViewHolder>{

    private final ArrayList<PostManager.Post> posts;
    public Context context;

    public RVAdapter(ArrayList<PostManager.Post> posts, Context context) {
        this.posts = posts;
        this.context = context;
    }

    public static class MaterialViewHolder extends RecyclerView.ViewHolder{
        Context context;
        CardView cv;
        TextView matTitle;
        TextView username;
        ImageView matPhoto;
        PostManager.Post currentPost;

        MaterialViewHolder(final View itemView, Context context) {
            super(itemView);
            this.context = context;
            cv = (CardView)itemView.findViewById(R.id.cv);
            matTitle = (TextView)itemView.findViewById(R.id.matTitle);
            username = (TextView)itemView.findViewById(R.id.username);
            matPhoto = (ImageView)itemView.findViewById(R.id.matPhoto);

            itemView.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    // item clicked
                    Log.d("ASDF", "title: " + currentPost.getTitle());
                    open(itemView);
                }
            });
        }

        public void open(View view){
            AlertDialog.Builder alertDialogBuilder = new AlertDialog.Builder(context);
            alertDialogBuilder.setTitle(currentPost.getTitle());
            alertDialogBuilder.setMessage(String.format("%s", currentPost.getMsg()));
            alertDialogBuilder.setCancelable(true);

            alertDialogBuilder.setNeutralButton("Geri", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {

                }
            });

            alertDialogBuilder.setPositiveButton("Yayınla", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface arg0, int arg1) {
                    String jout = JsonParser.instantiate.publishPostString(currentPost);
                    new RESTClient.PUTOperation().execute(jout, String.valueOf(currentPost.getId()));

                }
            });

            alertDialogBuilder.setNegativeButton("Sil",new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    new RESTClient.DELETEOperation().execute(String.valueOf(currentPost.getId()));
                }
            });

            AlertDialog alertDialog = alertDialogBuilder.create();
            alertDialog.show();
        }

    }

    @Override
    public void onAttachedToRecyclerView(RecyclerView recyclerView) {
        super.onAttachedToRecyclerView(recyclerView);
    }

    @Override
    public MaterialViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.list_item, parent, false);
        MaterialViewHolder pvh = new MaterialViewHolder(v,context);
        return pvh;
    }

    @Override
    public void onBindViewHolder(MaterialViewHolder holder, int position) {
        holder.matTitle.setText(PostManager.POSTS.get(position).getTitle());
        //holder.username.setText(PostManager.POSTS.get(position).getUser());
        holder.currentPost = PostManager.POSTS.get(position);
        // holder.matPhoto.setImageResource(PostManager.POSTS.get(position).);

    }

    @Override
    public int getItemCount() {
        return PostManager.getId_posts();
    }
}