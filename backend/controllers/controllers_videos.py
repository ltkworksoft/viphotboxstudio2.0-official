from sqlalchemy import desc, asc
from backend.app import db
from backend.models.models_videos import Videos, video_schema, videos_schema


class VideosControllers:
    @staticmethod
    def get_all_videos():
        return videos_schema.dump(Videos.query.order_by(desc(Videos.id)).all())

    @staticmethod
    def get_videos(limit):
        return videos_schema.dump(Videos.query.order_by(asc(Videos.time_added)).limit(limit))

    @staticmethod
    def get_video(link):
        return video_schema.jsonify(Videos.query.filter_by(link=link).first())

    def add_video(self, link, displayed, displayed_on):
        vid = self.get_video(link)
        if vid:
            return False
        new_video = Videos(
            link=link,
            displayed=displayed,
            displayed_on=displayed_on
        )
        db.session.add(new_video)
        db.session.commit()
        return True

    def modify_video(self, link, new_link, displayed, displayed_on):
        video = self.get_video(link)
        if video:
            video.link = new_link
            video.displayed = displayed
            video.displayed_on = displayed_on

            db.session.add(video)
            db.session.commit()
            return True
        return False

    def delete_video(self, link):
        video = self.get_video(link)
        if video:
            db.session.delete(video)
            db.session.commit()
            return True
        return False
