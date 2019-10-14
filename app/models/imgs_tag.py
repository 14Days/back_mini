import sqlalchemy as sa

metadata = sa.MetaData()

imgs_tag = sa.Table(
    'imgs_tag', metadata,
    sa.Column('img_id', sa.INT, primary_key=True, nullable=False, ForeignKey='Imgs.id'),
    sa.Column('tag_id', sa.INT, primary_key=True, nullable=False, default=0, ForeignKey='SecondLevel.id')
)
