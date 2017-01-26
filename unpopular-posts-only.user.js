// ==UserScript==
// @name        unpopular-posts-only
// @namespace   all-hail.lord-enki.net
// @description Remove posts from dash if they have too many notes
// @include     https://www.tumblr.com/dashboard
// @version     1
// @grant       none
// ==/UserScript==

function remove_popular_posts(){
  console.log("Starting up unpopular-posts-only...\n")
  
  
  notes_to_remove=[]
  note_counts=document.getElementsByClassName("note_link_current")
  
  console.log("Checking the number of notes for "+String(note_counts.length)+" posts.\n")
  
  for (i=0; i<note_counts.length; i++) {
   note=note_counts.item(i)
   c=parseInt(note.getAttribute("data-count"))
   if(c>1000) {
     console.log("Post to remove has "+String(c)+" notes.\n")
     notes_to_remove.push(note)
     
   }
  }

  console.log("Removing "+String(notes_to_remove.length)+" posts.\n")

  for (i=0; i<notes_to_remove.length; i++) {
  
   note=notes_to_remove[i]
   // post_container -> post_full -> post_wrapper -> post_footer -> post_notes -> post_notes_inner -> post_notes_label -> note_link_current
   
   post_notes_label=note.parentElement
   post_notes_inner=post_notes_label.parentElement
   post_notes=post_notes_inner.parentElement
   post_footer=post_notes.parentElement
   post_wrapper=post_footer.parentElement
   post_full=post_wrapper.parentElement
   post_container=post_full.parentElement
   
   //post_container.style.visibility="hidden";
   //post_container.style.maxHeight=0;
   post_full.style.opacity=0.25
   console.log("Removed post\n")
  }
  console.log("Done removing posts")
}

remove_popular_posts()
// From: https://stackoverflow.com/questions/28194122/how-to-execute-a-greasemonkey-script-on-every-infinite-scrolling-event-in-a-twit
window.addEventListener('load', function() {
       console.log("Load event triggered")
       remove_popular_posts()
    },
    false);
console.log("Got here")