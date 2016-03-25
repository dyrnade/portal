package com.sosyalyardimlasma.adminpaneli;

import java.util.ArrayList;

public class PostManager {

    public static int id_posts = 0;
    public static ArrayList<Post> POSTS = new ArrayList<Post>();
/*
    static {
        for(int i = 0; i < 5; i++) {
            add_post(new Post(i, "Title"+i, "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,"+i));
        }
    }
*/

    public static void clearPosts() {
        POSTS.clear();
        id_posts = 0;
    }

    public static void add_post(Post post){
        id_posts++;
        POSTS.add(post);
    }
    public static void delete_post(Post post) {
        POSTS.remove(post);
    }
/*
    public static Post find_post(String user, String title) {
        for(Post mypost : POSTS) {
            if(mypost.getTitle().equals(title) &&
                    mypost.getUser().equals(user)) {
                return mypost;
            }
        }
        return null;
    }
*/
    public static int getId_posts() {
        return id_posts;
    }

    public static class Post {
        int id;
        String title = "";
        String msg = "";
        Boolean published = false;

        public Post(int id, String title, String msg) {
            this.id = id;
            this.title = title;
            this.msg = msg;
        }

        public int getId() {
            return id;
        }


        public String getTitle() {
            return title;
        }

        public String getMsg() {
            return msg;
        }

        public Boolean getPublished() {
            return published;
        }

        public void setId(int id) {
            this.id = id;
        }


        public void setTitle(String title) {
            this.title = title;
        }

        public void setMsg(String msg) {
            this.msg = msg;
        }

        public void setPublished(Boolean published) {
            this.published = published;
        }
    }
}
